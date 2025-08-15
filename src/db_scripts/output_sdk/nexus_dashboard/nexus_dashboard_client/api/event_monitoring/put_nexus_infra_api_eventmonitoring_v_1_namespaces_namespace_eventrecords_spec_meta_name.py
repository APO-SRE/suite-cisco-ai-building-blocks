from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_record_v1_eventmonitoring_get import EventRecordV1EventmonitoringGET
from ...models.event_record_v1_eventmonitoring_put import EventRecordV1EventmonitoringPUT
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace: str,
    spec_meta_name: str,
    *,
    body: EventRecordV1EventmonitoringPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_nd_rbac, Unset):
        headers["X-Nd-Rbac"] = x_nd_rbac

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/nexus/infra/api/eventmonitoring/v1/namespaces/{namespace}/eventrecords/{spec_meta_name}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventRecordV1EventmonitoringGET]]:
    if response.status_code == 200:
        response_200 = EventRecordV1EventmonitoringGET.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, EventRecordV1EventmonitoringGET]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    namespace: str,
    spec_meta_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EventRecordV1EventmonitoringPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EventRecordV1EventmonitoringGET]]:
    """Modify an event record

     Modify an event record

    Args:
        namespace (str):
        spec_meta_name (str):
        x_nd_rbac (Union[Unset, str]):
        body (EventRecordV1EventmonitoringPUT): An event monitoring record gets generated on a
            resource that is crossing the threshold set in the parent event configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRecordV1EventmonitoringGET]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        spec_meta_name=spec_meta_name,
        body=body,
        x_nd_rbac=x_nd_rbac,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    namespace: str,
    spec_meta_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EventRecordV1EventmonitoringPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EventRecordV1EventmonitoringGET]]:
    """Modify an event record

     Modify an event record

    Args:
        namespace (str):
        spec_meta_name (str):
        x_nd_rbac (Union[Unset, str]):
        body (EventRecordV1EventmonitoringPUT): An event monitoring record gets generated on a
            resource that is crossing the threshold set in the parent event configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventRecordV1EventmonitoringGET]
    """

    return sync_detailed(
        namespace=namespace,
        spec_meta_name=spec_meta_name,
        client=client,
        body=body,
        x_nd_rbac=x_nd_rbac,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    spec_meta_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EventRecordV1EventmonitoringPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EventRecordV1EventmonitoringGET]]:
    """Modify an event record

     Modify an event record

    Args:
        namespace (str):
        spec_meta_name (str):
        x_nd_rbac (Union[Unset, str]):
        body (EventRecordV1EventmonitoringPUT): An event monitoring record gets generated on a
            resource that is crossing the threshold set in the parent event configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventRecordV1EventmonitoringGET]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        spec_meta_name=spec_meta_name,
        body=body,
        x_nd_rbac=x_nd_rbac,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    namespace: str,
    spec_meta_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EventRecordV1EventmonitoringPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EventRecordV1EventmonitoringGET]]:
    """Modify an event record

     Modify an event record

    Args:
        namespace (str):
        spec_meta_name (str):
        x_nd_rbac (Union[Unset, str]):
        body (EventRecordV1EventmonitoringPUT): An event monitoring record gets generated on a
            resource that is crossing the threshold set in the parent event configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventRecordV1EventmonitoringGET]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            spec_meta_name=spec_meta_name,
            client=client,
            body=body,
            x_nd_rbac=x_nd_rbac,
        )
    ).parsed
