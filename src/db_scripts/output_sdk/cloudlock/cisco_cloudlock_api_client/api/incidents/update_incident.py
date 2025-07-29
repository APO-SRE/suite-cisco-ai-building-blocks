from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incidents_collection import IncidentsCollection
from ...models.update_incident_body import UpdateIncidentBody
from ...models.update_incident_response_400 import UpdateIncidentResponse400
from ...models.update_incident_response_401 import UpdateIncidentResponse401
from ...models.update_incident_response_403 import UpdateIncidentResponse403
from ...models.update_incident_response_404 import UpdateIncidentResponse404
from ...models.update_incident_response_500 import UpdateIncidentResponse500
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: UpdateIncidentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/incidents/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        IncidentsCollection,
        UpdateIncidentResponse400,
        UpdateIncidentResponse401,
        UpdateIncidentResponse403,
        UpdateIncidentResponse404,
        UpdateIncidentResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = IncidentsCollection.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = UpdateIncidentResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = UpdateIncidentResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = UpdateIncidentResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = UpdateIncidentResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = UpdateIncidentResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        IncidentsCollection,
        UpdateIncidentResponse400,
        UpdateIncidentResponse401,
        UpdateIncidentResponse403,
        UpdateIncidentResponse404,
        UpdateIncidentResponse500,
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
    body: UpdateIncidentBody,
) -> Response[
    Union[
        IncidentsCollection,
        UpdateIncidentResponse400,
        UpdateIncidentResponse401,
        UpdateIncidentResponse403,
        UpdateIncidentResponse404,
        UpdateIncidentResponse500,
    ]
]:
    """Update Incident

     Update a specific incident.

    Args:
        id (int):
        body (UpdateIncidentBody):  Example: {'incident_status': 'RESOLVED'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IncidentsCollection, UpdateIncidentResponse400, UpdateIncidentResponse401, UpdateIncidentResponse403, UpdateIncidentResponse404, UpdateIncidentResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateIncidentBody,
) -> Optional[
    Union[
        IncidentsCollection,
        UpdateIncidentResponse400,
        UpdateIncidentResponse401,
        UpdateIncidentResponse403,
        UpdateIncidentResponse404,
        UpdateIncidentResponse500,
    ]
]:
    """Update Incident

     Update a specific incident.

    Args:
        id (int):
        body (UpdateIncidentBody):  Example: {'incident_status': 'RESOLVED'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IncidentsCollection, UpdateIncidentResponse400, UpdateIncidentResponse401, UpdateIncidentResponse403, UpdateIncidentResponse404, UpdateIncidentResponse500]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateIncidentBody,
) -> Response[
    Union[
        IncidentsCollection,
        UpdateIncidentResponse400,
        UpdateIncidentResponse401,
        UpdateIncidentResponse403,
        UpdateIncidentResponse404,
        UpdateIncidentResponse500,
    ]
]:
    """Update Incident

     Update a specific incident.

    Args:
        id (int):
        body (UpdateIncidentBody):  Example: {'incident_status': 'RESOLVED'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IncidentsCollection, UpdateIncidentResponse400, UpdateIncidentResponse401, UpdateIncidentResponse403, UpdateIncidentResponse404, UpdateIncidentResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateIncidentBody,
) -> Optional[
    Union[
        IncidentsCollection,
        UpdateIncidentResponse400,
        UpdateIncidentResponse401,
        UpdateIncidentResponse403,
        UpdateIncidentResponse404,
        UpdateIncidentResponse500,
    ]
]:
    """Update Incident

     Update a specific incident.

    Args:
        id (int):
        body (UpdateIncidentBody):  Example: {'incident_status': 'RESOLVED'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IncidentsCollection, UpdateIncidentResponse400, UpdateIncidentResponse401, UpdateIncidentResponse403, UpdateIncidentResponse404, UpdateIncidentResponse500]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
