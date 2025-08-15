from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_aggregates import IncidentAggregates
from ...models.list_incident_aggregates_policies_response_400 import ListIncidentAggregatesPoliciesResponse400
from ...models.list_incident_aggregates_policies_response_401 import ListIncidentAggregatesPoliciesResponse401
from ...models.list_incident_aggregates_policies_response_403 import ListIncidentAggregatesPoliciesResponse403
from ...models.list_incident_aggregates_policies_response_404 import ListIncidentAggregatesPoliciesResponse404
from ...models.list_incident_aggregates_policies_response_500 import ListIncidentAggregatesPoliciesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_after: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    policies: Union[Unset, str] = UNSET,
    users: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["created_after"] = created_after

    params["vendor"] = vendor

    params["order"] = order

    params["policies"] = policies

    params["users"] = users

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/incidents/aggregates/policies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListIncidentAggregatesPoliciesResponse400,
        ListIncidentAggregatesPoliciesResponse401,
        ListIncidentAggregatesPoliciesResponse403,
        ListIncidentAggregatesPoliciesResponse404,
        ListIncidentAggregatesPoliciesResponse500,
        list["IncidentAggregates"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IncidentAggregates.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListIncidentAggregatesPoliciesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListIncidentAggregatesPoliciesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListIncidentAggregatesPoliciesResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListIncidentAggregatesPoliciesResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListIncidentAggregatesPoliciesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListIncidentAggregatesPoliciesResponse400,
        ListIncidentAggregatesPoliciesResponse401,
        ListIncidentAggregatesPoliciesResponse403,
        ListIncidentAggregatesPoliciesResponse404,
        ListIncidentAggregatesPoliciesResponse500,
        list["IncidentAggregates"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_after: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    policies: Union[Unset, str] = UNSET,
    users: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListIncidentAggregatesPoliciesResponse400,
        ListIncidentAggregatesPoliciesResponse401,
        ListIncidentAggregatesPoliciesResponse403,
        ListIncidentAggregatesPoliciesResponse404,
        ListIncidentAggregatesPoliciesResponse500,
        list["IncidentAggregates"],
    ]
]:
    """List Incident Aggregates Policies

     Get the aggregations (by policies/users/status) for the incidents.

    Args:
        created_after (Union[Unset, str]):
        vendor (Union[Unset, str]):
        order (Union[Unset, str]):
        policies (Union[Unset, str]):
        users (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListIncidentAggregatesPoliciesResponse400, ListIncidentAggregatesPoliciesResponse401, ListIncidentAggregatesPoliciesResponse403, ListIncidentAggregatesPoliciesResponse404, ListIncidentAggregatesPoliciesResponse500, list['IncidentAggregates']]]
    """

    kwargs = _get_kwargs(
        created_after=created_after,
        vendor=vendor,
        order=order,
        policies=policies,
        users=users,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    created_after: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    policies: Union[Unset, str] = UNSET,
    users: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListIncidentAggregatesPoliciesResponse400,
        ListIncidentAggregatesPoliciesResponse401,
        ListIncidentAggregatesPoliciesResponse403,
        ListIncidentAggregatesPoliciesResponse404,
        ListIncidentAggregatesPoliciesResponse500,
        list["IncidentAggregates"],
    ]
]:
    """List Incident Aggregates Policies

     Get the aggregations (by policies/users/status) for the incidents.

    Args:
        created_after (Union[Unset, str]):
        vendor (Union[Unset, str]):
        order (Union[Unset, str]):
        policies (Union[Unset, str]):
        users (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListIncidentAggregatesPoliciesResponse400, ListIncidentAggregatesPoliciesResponse401, ListIncidentAggregatesPoliciesResponse403, ListIncidentAggregatesPoliciesResponse404, ListIncidentAggregatesPoliciesResponse500, list['IncidentAggregates']]
    """

    return sync_detailed(
        client=client,
        created_after=created_after,
        vendor=vendor,
        order=order,
        policies=policies,
        users=users,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_after: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    policies: Union[Unset, str] = UNSET,
    users: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListIncidentAggregatesPoliciesResponse400,
        ListIncidentAggregatesPoliciesResponse401,
        ListIncidentAggregatesPoliciesResponse403,
        ListIncidentAggregatesPoliciesResponse404,
        ListIncidentAggregatesPoliciesResponse500,
        list["IncidentAggregates"],
    ]
]:
    """List Incident Aggregates Policies

     Get the aggregations (by policies/users/status) for the incidents.

    Args:
        created_after (Union[Unset, str]):
        vendor (Union[Unset, str]):
        order (Union[Unset, str]):
        policies (Union[Unset, str]):
        users (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListIncidentAggregatesPoliciesResponse400, ListIncidentAggregatesPoliciesResponse401, ListIncidentAggregatesPoliciesResponse403, ListIncidentAggregatesPoliciesResponse404, ListIncidentAggregatesPoliciesResponse500, list['IncidentAggregates']]]
    """

    kwargs = _get_kwargs(
        created_after=created_after,
        vendor=vendor,
        order=order,
        policies=policies,
        users=users,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    created_after: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    policies: Union[Unset, str] = UNSET,
    users: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListIncidentAggregatesPoliciesResponse400,
        ListIncidentAggregatesPoliciesResponse401,
        ListIncidentAggregatesPoliciesResponse403,
        ListIncidentAggregatesPoliciesResponse404,
        ListIncidentAggregatesPoliciesResponse500,
        list["IncidentAggregates"],
    ]
]:
    """List Incident Aggregates Policies

     Get the aggregations (by policies/users/status) for the incidents.

    Args:
        created_after (Union[Unset, str]):
        vendor (Union[Unset, str]):
        order (Union[Unset, str]):
        policies (Union[Unset, str]):
        users (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListIncidentAggregatesPoliciesResponse400, ListIncidentAggregatesPoliciesResponse401, ListIncidentAggregatesPoliciesResponse403, ListIncidentAggregatesPoliciesResponse404, ListIncidentAggregatesPoliciesResponse500, list['IncidentAggregates']]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_after=created_after,
            vendor=vendor,
            order=order,
            policies=policies,
            users=users,
            status=status,
        )
    ).parsed
