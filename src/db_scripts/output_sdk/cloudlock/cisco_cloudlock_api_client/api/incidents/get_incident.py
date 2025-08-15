from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_incident_response_400 import GetIncidentResponse400
from ...models.get_incident_response_401 import GetIncidentResponse401
from ...models.get_incident_response_403 import GetIncidentResponse403
from ...models.get_incident_response_404 import GetIncidentResponse404
from ...models.get_incident_response_500 import GetIncidentResponse500
from ...models.incidents_collection import IncidentsCollection
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/incidents/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetIncidentResponse400,
        GetIncidentResponse401,
        GetIncidentResponse403,
        GetIncidentResponse404,
        GetIncidentResponse500,
        IncidentsCollection,
    ]
]:
    if response.status_code == 200:
        response_200 = IncidentsCollection.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetIncidentResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GetIncidentResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = GetIncidentResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = GetIncidentResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GetIncidentResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetIncidentResponse400,
        GetIncidentResponse401,
        GetIncidentResponse403,
        GetIncidentResponse404,
        GetIncidentResponse500,
        IncidentsCollection,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        GetIncidentResponse400,
        GetIncidentResponse401,
        GetIncidentResponse403,
        GetIncidentResponse404,
        GetIncidentResponse500,
        IncidentsCollection,
    ]
]:
    """Get Incident

     Get the information about a specific incident.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetIncidentResponse400, GetIncidentResponse401, GetIncidentResponse403, GetIncidentResponse404, GetIncidentResponse500, IncidentsCollection]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        GetIncidentResponse400,
        GetIncidentResponse401,
        GetIncidentResponse403,
        GetIncidentResponse404,
        GetIncidentResponse500,
        IncidentsCollection,
    ]
]:
    """Get Incident

     Get the information about a specific incident.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetIncidentResponse400, GetIncidentResponse401, GetIncidentResponse403, GetIncidentResponse404, GetIncidentResponse500, IncidentsCollection]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        GetIncidentResponse400,
        GetIncidentResponse401,
        GetIncidentResponse403,
        GetIncidentResponse404,
        GetIncidentResponse500,
        IncidentsCollection,
    ]
]:
    """Get Incident

     Get the information about a specific incident.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetIncidentResponse400, GetIncidentResponse401, GetIncidentResponse403, GetIncidentResponse404, GetIncidentResponse500, IncidentsCollection]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        GetIncidentResponse400,
        GetIncidentResponse401,
        GetIncidentResponse403,
        GetIncidentResponse404,
        GetIncidentResponse500,
        IncidentsCollection,
    ]
]:
    """Get Incident

     Get the information about a specific incident.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetIncidentResponse400, GetIncidentResponse401, GetIncidentResponse403, GetIncidentResponse404, GetIncidentResponse500, IncidentsCollection]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
